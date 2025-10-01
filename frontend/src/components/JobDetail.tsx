import React from 'react'
import { useParams, Link } from 'react-router-dom'
import { ArrowLeft, Play, Edit, Trash2, Clock } from 'lucide-react'

const JobDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>()

  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-4">
        <Link to="/jobs" className="text-gray-600 hover:text-gray-900">
          <ArrowLeft size={20} />
        </Link>
        <h1 className="text-3xl font-bold text-gray-900">Job Details</h1>
      </div>

      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4 border-b border-gray-200">
          <div className="flex justify-between items-center">
            <h2 className="text-lg font-medium text-gray-900">Job #{id}</h2>
            <div className="flex space-x-2">
              <button className="bg-green-600 text-white px-3 py-1 rounded flex items-center space-x-1 text-sm">
                <Play size={16} />
                <span>Run</span>
              </button>
              <button className="bg-blue-600 text-white px-3 py-1 rounded flex items-center space-x-1 text-sm">
                <Edit size={16} />
                <span>Edit</span>
              </button>
              <button className="bg-red-600 text-white px-3 py-1 rounded flex items-center space-x-1 text-sm">
                <Trash2 size={16} />
                <span>Delete</span>
              </button>
            </div>
          </div>
        </div>
        
        <div className="p-6">
          <div className="text-center py-8">
            <Clock className="mx-auto h-12 w-12 text-gray-400" />
            <h3 className="mt-2 text-sm font-medium text-gray-900">No job data</h3>
            <p className="mt-1 text-sm text-gray-500">Job details will be loaded when the backend is connected.</p>
          </div>
        </div>
      </div>

      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-medium text-gray-900">Execution History</h2>
        </div>
        <div className="p-6">
          <p className="text-gray-500 text-center py-8">No executions yet</p>
        </div>
      </div>
    </div>
  )
}

export default JobDetail