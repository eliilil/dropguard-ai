import { PieChart, Pie, Cell, Tooltip, Legend } from "recharts"

const COLORS = ["#A8D8EA", "#D4B5F0", "#FFB6C1", "#FFD4B2"]

export default function BurnoutPie({ data }) {

  if (!data || data.length === 0) {
    return <p className="text-center text-gray-500">No burnout data</p>
  }

  return (
    <PieChart width={350} height={250}>
      <Pie
        data={data}
        dataKey="value"
        nameKey="name"
        outerRadius={90}
        label
      >
        {data.map((entry, index) => (
          <Cell
            key={index}
            fill={COLORS[index % COLORS.length]}
          />
        ))}
      </Pie>

      <Tooltip />
      <Legend />

    </PieChart>
  )
}