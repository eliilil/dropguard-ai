import { PieChart, Pie, Tooltip, Cell } from "recharts";

export default function BurnoutPie({ data }) {

  if (!data || data.length === 0) return <p>No burnout data</p>;

  const chartData = [
    {
      name: "Low Risk",
      value: data.filter(s => s.burnout_risk < 40).length
    },
    {
      name: "Medium Risk",
      value: data.filter(s => s.burnout_risk >= 40 && s.burnout_risk < 80).length
    },
    {
      name: "High Risk",
      value: data.filter(s => s.burnout_risk >= 80).length
    }
  ];

  return (
    <PieChart width={300} height={300}>
      <Pie data={chartData} dataKey="value" nameKey="name">
        {chartData.map((entry, index) => (
          <Cell key={index} />
        ))}
      </Pie>
      <Tooltip />
    </PieChart>
  );
}