import React from "react";

interface ButtonProps {
  children: React.ReactNode;
  className?: string;
  onClick?: () => void;
  type?: "button" | "submit" | "reset";
}

function Button({ ...props }: ButtonProps) {
  return (
    <button
      className={`px-5 py-2 rounded-md bg-slate-900 hover:bg-slate-500 text-white w-full ${props.className}`}
      {...props}
    >
      {props.children}
    </button>
  );
}

export default Button;
