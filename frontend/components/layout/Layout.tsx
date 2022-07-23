import Sidebar from "../sidebar/Sidebar";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex">
      <Sidebar />
      <div className="py-10 px-8">
        {children}
      </div>
    </div>
  )
}