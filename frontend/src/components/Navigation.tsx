import React from 'react'
import { Link, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { Home, Briefcase, LogOut, User } from 'lucide-react'

const Navigation: React.FC = () => {
  const { user, logout } = useAuth()
  const location = useLocation()

  const isActive = (path: string) => location.pathname === path

  return (
    <nav className="w-64 bg-white shadow-lg h-screen">
      <div className="p-6">
        <h1 className="text-xl font-bold text-gray-800">Webscraping Platform</h1>
      </div>
      
      <div className="px-6 py-2">
        <div className="flex items-center space-x-2 text-sm text-gray-600">
          <User size={16} />
          <span>{user?.email}</span>
        </div>
      </div>

      <ul className="mt-6">
        <li>
          <Link
            to="/"
            className={`flex items-center px-6 py-3 text-sm ${
              isActive('/') 
                ? 'bg-blue-50 text-blue-600 border-r-2 border-blue-600' 
                : 'text-gray-600 hover:bg-gray-50'
            }`}
          >
            <Home size={18} className="mr-3" />
            Dashboard
          </Link>
        </li>
        <li>
          <Link
            to="/jobs"
            className={`flex items-center px-6 py-3 text-sm ${
              isActive('/jobs') 
                ? 'bg-blue-50 text-blue-600 border-r-2 border-blue-600' 
                : 'text-gray-600 hover:bg-gray-50'
            }`}
          >
            <Briefcase size={18} className="mr-3" />
            Jobs
          </Link>
        </li>
      </ul>

      <div className="absolute bottom-0 w-64 p-6">
        <button
          onClick={logout}
          className="flex items-center w-full px-4 py-2 text-sm text-gray-600 hover:bg-gray-50 rounded-lg"
        >
          <LogOut size={18} className="mr-3" />
          Logout
        </button>
      </div>
    </nav>
  )
}

export default Navigation