import { useState } from "react"

export default function StudentTable({ students }) {

  const [search,setSearch] = useState("")

  const filtered = students.filter(
    s =>
      s.name.toLowerCase().includes(search.toLowerCase()) ||
      s.student_id.toLowerCase().includes(search.toLowerCase())
  )

  return (
    <div className="bg-white rounded-xl shadow p-6 mt-6">

      <input
        type="text"
        placeholder="Search by name or ID..."
        className="border p-2 rounded mb-4 w-full"
        onChange={(e)=>setSearch(e.target.value)}
      />

      <table className="w-full">

        <thead>
          <tr className="border-b text-left">
            <th>ID</th>
            <th>Name</th>
            <th>Attendance</th>
            <th>Burnout</th>
            <th>Sleep</th>
          </tr>
        </thead>

        <tbody>

          {filtered.slice(0,20).map(student => (

            <tr key={student.student_id} className="border-b hover:bg-gray-50">

              <td>{student.student_id}</td>
              <td>{student.name}</td>
              <td>{student.attendance_pct}%</td>
              <td>{student.burnout_risk}</td>
              <td>{student.avg_sleep_hours}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  )
}