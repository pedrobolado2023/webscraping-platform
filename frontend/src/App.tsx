import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import JobList from './components/JobList'
import JobDetail from './components/JobDetail'
import Navigation from './components/Navigation'
import { AuthProvider, useAuth } from './context/AuthContext'

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <div className="min-h-screen bg-gray-50">
          <AppRoutes />
        </div>
      </AuthProvider>
    </BrowserRouter>
  )
}

function AppRoutes() {
  const { isAuthenticated } = useAuth()

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Login />
      </div>
    )
  }

  return (
    <div className="flex">
      <Navigation />
      <main className="flex-1 p-6">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/jobs" element={<JobList />} />
          <Route path="/jobs/:id" element={<JobDetail />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </main>
    </div>
  )
}

export default App