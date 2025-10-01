import React from 'react'
import { Plus } from 'lucide-react'

const JobList: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Jobs</h1>
        <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 flex items-center space-x-2">
          <Plus size={18} />
          <span>Create Job</span>
        </button>
      </div>

      <div className="bg-white shadow rounded-lg">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-lg font-medium text-gray-900">Your Jobs</h2>
        </div>
        <div className="p-6">
          <div className="text-center py-8">
            <div className="mx-auto h-12 w-12 text-gray-400">
              <svg fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h3 className="mt-2 text-sm font-medium text-gray-900">No jobs yet</h3>
            <p className="mt-1 text-sm text-gray-500">Get started by creating your first scraping job.</p>
            <div className="mt-6">
              <button className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 flex items-center space-x-2 mx-auto">
                <Plus size={18} />
                <span>Create your first job</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default JobList