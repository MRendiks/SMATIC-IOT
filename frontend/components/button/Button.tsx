import { forwardRef } from "react";
import classmerge from "../../lib/classmerge";

type ButtonProps = {
  variant?: 'primary' | 'outline';
} & React.ComponentPropsWithRef<'button'>;

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ children, variant, ...rest }, ref) => (
    <button 
      ref={ref}
      className={
        classmerge(
          'py-3 px-5 rounded-md font-semibold',
          [
            variant === 'primary' && [
              'bg-gradient-to-l from-primary to-primary/50 inline-block text-white'
            ]
          ]
        )
      }
      {...rest}
    >
      {children}
    </button>
  )
)

Button.displayName = 'Button';

export default Button;