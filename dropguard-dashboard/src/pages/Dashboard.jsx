import { useEffect, useState } from "react"

import { getOverview, getHighRiskStudents, getStudents } from "../services/api"

import StatCard from "../components/StatCard"
import HighRiskAlert from "../components/HighRiskAlert"
import StudentTable from "../components/StudentTable"

import BurnoutPie from "../charts/BurnoutPie"
import AttendanceBar from "../charts/AttendanceBar"
import LibrarySleepScatter from "../charts/LibrarySleepScatter"

export default function Dashboard() {

  const [overview, setOverview] = useState({})
  const [highRisk, setHighRisk] = useState([])
  const [students, setStudents] = useState([])
  const [loading, setLoading] = useState(true)

  const fetchData = async () => {

    try {

      const overviewRes = await getOverview()
      const highRiskRes = await getHighRiskStudents()
      const studentsRes = await getStudents()

      console.log("Overview API:", overviewRes.data)
      console.log("High Risk API:", highRiskRes.data)
      console.log("Students API:", studentsRes.data)

      const overviewData = overviewRes?.data || {}

      const highRiskData =
        highRiskRes?.data?.students ||
        highRiskRes?.data ||
        []

      const studentData =
        studentsRes?.data?.students ||
        studentsRes?.data ||
        []

      setOverview(overviewData)
      setHighRisk(highRiskData)
      setStudents(studentData)

      setLoading(false)

    } catch (error) {

      console.error("API fetch error:", error)

      setOverview({})
      setHighRisk([])
      setStudents([])
      setLoading(false)

    }

  }

  useEffect(() => {

    const loadData = async () => {
      await fetchData()
    }

    loadData()

    const interval = setInterval(loadData, 30000)

    return () => clearInterval(interval)

  }, [])

  /* Loading Screen */

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen text-xl font-semibold">
        Loading DropGuard AI Dashboard...
      </div>
    )
  }

  return (

    <div className="min-h-screen p-8 bg-gradient-to-br from-[#FFD4B2] to-[#A8D8EA]">

      <HighRiskAlert students={highRisk || []} />

      {/* Stat Cards */}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">

        <StatCard
          title="Total Students"
          value={overview?.total_students || students.length || 0}
          color="border-blue-400"
        />

        <StatCard
          title="Average Attendance"
          value={overview?.avg_attendance || 0}
          color="border-purple-400"
        />

        <StatCard
          title="High Risk Students"
          value={overview?.high_risk_students || highRisk.length || 0}
          color="border-red-400"
        />

        <StatCard
          title="Medical Issues"
          value={overview?.medical_cases || 0}
          color="border-pink-400"
        />

      </div>

      {/* Charts */}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-10">

        <div className="bg-white rounded-xl shadow p-4">
          <h2 className="font-semibold mb-2">Burnout Risk Distribution</h2>
          <BurnoutPie data={overview?.burnout_distribution || []} />
        </div>

        <div className="bg-white rounded-xl shadow p-4">
          <h2 className="font-semibold mb-2">Attendance Distribution</h2>
          <AttendanceBar data={overview?.attendance_distribution || []} />
        </div>

        <div className="bg-white rounded-xl shadow p-4">
          <h2 className="font-semibold mb-2">Library vs Sleep Correlation</h2>
          <LibrarySleepScatter data={students || []} />
        </div>

      </div>

      {/* Student Table */}

      <StudentTable students={students || []} />

    </div>

  )

}