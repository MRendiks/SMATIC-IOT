import Image from "next/image";
import MenuItem from "./MenuItem";

const SidebarMenuItem = [
  {
    title: 'Dashboard',
    icon: '/assets/dashboard-icon.svg',
    isActive: true,
  },
  {
    title: 'Logistic',
    icon: '/assets/logistic-icon.svg',
    isActive: false,
  },
  {
    title: 'User Charge',
    icon: '/assets/user-charge-icon.svg',
    isActive: false,
  },
  {
    title: 'Settings',
    icon: '/assets/settings-icon.svg',
    isActive: false,
  }
];

export default function Sidebar() {
  return (
    <div className="bg-white h-screen w-[300px] shrink-0 sticky top-0">
      <div className="p-[50px]">
        <Image 
          src="/assets/main-logo.png" 
          width="164" 
          height="45" 
          alt="Smatic Logo" 
        />
      </div>
      <div>
        <ul className="px-8 w-full">
          {
            SidebarMenuItem.map(menu => (
              <li key={menu.title} className="my-5">
                <MenuItem title={menu.title} icon={menu.icon} isActive={menu.isActive} />
              </li>
            ))
          }
        </ul>
      </div>
    </div>
  )
}