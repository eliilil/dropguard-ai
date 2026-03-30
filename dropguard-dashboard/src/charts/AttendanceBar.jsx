import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts"

export default function AttendanceBar({ data }) {

  return (
    <BarChart width={400} height={250} data={data}>
      <XAxis dataKey="range" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="students" fill="#B8E0F6" />
    </BarChart>
  )

}