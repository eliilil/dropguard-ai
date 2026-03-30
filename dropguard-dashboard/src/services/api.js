import axios from "axios"

const API = axios.create({
  baseURL: "http://127.0.0.1:8001/api/v1"
})

// dashboard overview
export const getOverview = () => API.get("/analytics/overview")

// high risk students
export const getHighRiskStudents = () =>
  API.get("/analytics/high-risk-students")

// all students
export const getStudents = () => API.get("/students")

// search students
export const searchStudents = (query) =>
  API.get(`/students/search/${query}`)

export default API