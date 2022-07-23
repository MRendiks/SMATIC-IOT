import { forwardRef } from "react";

type InputProps = {} & React.ComponentPropsWithoutRef<'input'>;

const Input = forwardRef<HTMLInputElement, InputProps>(({...rest}, ref) => {
  return (
    <input 
      className="w-full px-4 py-3 outline-none rounded-md font-semibold placeholder:text-gray-400 text-secondary"
      ref={ref}
      {...rest}
    />
  )
})

Input.displayName = 'Input';

export default Input;