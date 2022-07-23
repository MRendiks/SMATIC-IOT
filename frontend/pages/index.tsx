import type { NextPage } from 'next'
import Image from 'next/image'
import Button from '../components/button/Button'
import Input from '../components/form/Input'
import Switch from '../components/form/Switch'
import Layout from '../components/layout/Layout'
import { deviceItems, rackItems } from '../data/item-table'
import classmerge from '../lib/classmerge'

const Home: NextPage = () => {
  return (
    <Layout>
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-4xl mb-2 font-semibold text-primary">
            Good Morning, Bambang
          </h1>
          <p className="text-lg font-medium text-primary">Have a nice day</p>
        </div>
        <div className="flex flex-nowrap">
          <div className="mr-3">
            <Button variant="primary">Perangkat Baru</Button>
          </div>
          <div className="ml-3">
            <Input placeholder="Search" />
          </div>
        </div>
      </div>
      <div className="mt-8 bg-white rounded-md p-3">
        <h4 className="text-lg font-extrabold text-primary">Conveyor</h4>
        <div className="grid grid-cols-4 mt-2 gap-x-4">
          <div className="bg-gradient-to-l from-primary to-primary/50 p-3 rounded-md flex flex-col justify-between">
            <Input value="7EHJ2999" onChange={() => {}} />
            <div className="mt-4 flex justify-between items-center">
              <h6 className="font-medium text-white">RFID Tag</h6>
              <div className="bg-white text-primary py-1 px-2 rounded-md">
                Detected
              </div>
            </div>
          </div>
          <div className="bg-gradient-to-l from-primary to-primary/50 p-3 rounded-md flex flex-col justify-between">
            <div className="flex items-center justify-between">
              <Image
                src="/assets/servo-icon.png"
                width={39}
                height={39}
                alt="Servo"
              />
              <Switch switchId="servo1" size="large" />
            </div>
            <div className="mt-4 flex justify-between items-center">
              <h6 className="font-medium text-white">Servo 1</h6>
              <div className="bg-white text-primary py-1 px-2 rounded-md">
                Detected
              </div>
            </div>
          </div>
          <div className="bg-gradient-to-l from-primary to-primary/50 p-3 rounded-md flex flex-col justify-between">
            <div className="flex items-center justify-between">
              <Image
                src="/assets/servo-icon.png"
                width={39}
                height={39}
                alt="Servo"
              />
              <Switch switchId="servo2" size="large" />
            </div>
            <div className="mt-4 flex justify-between items-center">
              <h6 className="font-medium text-white">Servo 2</h6>
              <div className="bg-white text-primary py-1 px-2 rounded-md">
                Detected
              </div>
            </div>
          </div>
          <div className="bg-gradient-to-l from-primary to-primary/50 p-3 rounded-md flex flex-col justify-between">
            <div className="flex items-center justify-between">
              <Image
                src="/assets/servo-icon.png"
                width={39}
                height={39}
                alt="Servo"
              />
              <Switch switchId="servo3" size="large" />
            </div>
            <div className="mt-4 flex justify-between items-center">
              <h6 className="font-medium text-white">Servo 3</h6>
              <div className="bg-white text-primary py-1 px-2 rounded-md">
                Detected
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="mt-8 grid grid-cols-2 gap-x-10">
        <div>
          <h4 className="text-lg font-extrabold text-primary">Device</h4>
          <div className="bg-white mt-3 p-2 rounded-md">
            <table className="w-full text-sm text-left text-gray-500 rounded">
              <thead className="text-xs text-white uppercase bg-primary">
                <tr>
                  <th className="px-6 py-3">ID</th>
                  <th className="px-6 py-3">Name</th>
                  <th className="px-6 py-3">Mac Address</th>
                  <th className="px-6 py-3">Status</th>
                </tr>
              </thead>
              <tbody>
                {deviceItems.map((item) => (
                  <tr
                    key={item.id}
                    className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                  >
                    <th className="px-6 py-4">{item.id}</th>
                    <td className="px-6 py-4">{item.name}</td>
                    <td className="px-6 py-4">{item.macAddress}</td>
                    <td className="px-6 py-4 text-center">
                      <Switch
                        switchId={`switch-device-${item.id}`}
                        size="small"
                      />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            <a href="#" className="text-primary text-sm text-center block py-4">
              View more
            </a>
          </div>
        </div>
        <div>
          <h4 className="text-lg font-extrabold text-primary">Rack</h4>
          <div className="bg-white mt-3 p-2 rounded-md">
            <table className="w-full text-sm text-left text-gray-500 rounded">
              <thead className="text-xs text-white uppercase bg-primary">
                <tr>
                  <th className="px-6 py-3">ID</th>
                  <th className="px-6 py-3">Name</th>
                  <th className="px-6 py-3">Distance</th>
                  <th className="px-6 py-3">Stock</th>
                </tr>
              </thead>
              <tbody>
                {rackItems.map((item) => (
                  <tr
                    key={item.id}
                    className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                  >
                    <th className="px-6 py-4">{item.id}</th>
                    <td className="px-6 py-4">{item.name}</td>
                    <td className="px-6 py-4">{item.distance}</td>
                    <td className="px-6 py-4 text-center">
                      <small
                        className={classmerge(
                          "text-[10px] rounded-full w-[40px] inline-block text-white",
                          [item.stock > 0 ? "bg-primary" : "bg-red-500"]
                        )}
                      >
                        {item.stock > 0 ? item.stock : "Full"}
                      </small>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
            <a href="#" className="text-primary text-sm text-center block py-4">
              View more
            </a>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default Home
