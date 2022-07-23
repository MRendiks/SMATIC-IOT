import classmerge from "../../lib/classmerge";

type SwitchProps = {
  switchId: string;
  isActive?: boolean;
  size: 'small' | 'large';
}

export default function Switch({ switchId, isActive, size }: SwitchProps) {
  return (
    <label
      htmlFor={switchId}
      className="inline-flex relative items-center cursor-pointer"
    >
      <input
        type="checkbox"
        value=""
        id={switchId}
        className="sr-only peer"
        checked={isActive}
      />
      <div
        className={classmerge(
          "border border-gray-300 bg-gray-300 peer-focus:outline-none",
          "rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white",
          "after:content-[''] after:absolute",
          "after:bg-red-400 peer-checked:after:bg-primary after:border-gray-300",
          "after:border after:rounded-full after:transition-all peer-checked:bg-white",
          [
            size === "large" && [
              "w-11 h-6 after:h-5 after:w-5 after:top-[2px] after:left-[2px]",
            ],
            size === "small" && [
              "w-8 h-4 after:h-3.5 after:w-3.5 after:top-[1px] after:left-[2px]",
            ],
          ]
        )}
      ></div>
    </label>
  );
}