import Image from "next/image";
import Link from "next/link";

type MenuItemProps = {
  title: string;
  icon: string;
  isActive: boolean;
}

export default function MenuItem({ title, icon, isActive }: MenuItemProps) {
  return (
    <Link href="/">
      <a className={`p-3 rounded-md w-full flex ${isActive && 'bg-gradient-to-l from-primary to-primary/50 text-white'}`}>
        <Image src={icon} width={24.57} height={24.57} className="fill-red-600" alt={`Icon ${title}`} />
        <span className={`block pl-4 font-semibold ${isActive ? 'text-white' : 'text-secondary'}`}>{title}</span>
      </a>
    </Link>
  )
}