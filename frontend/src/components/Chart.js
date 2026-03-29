import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale);

export default function Chart({ impact }) {
  const data = {
    labels: ["Monthly", "Yearly"],
    datasets: [
      {
        label: "Savings (₹)",
        data: [impact.monthly_savings, impact.yearly_savings],
      },
    ],
  };

  return <Bar data={data} />;
}