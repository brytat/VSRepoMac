import React from "react";

interface InputProps {
  className?: string;
  placeholder?: string;
  type?: "text" | "password" | "email";
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void; // Data binding
  error?: string;
  onBlur?: (e: React.FocusEvent<HTMLInputElement>) => void;
  value?: string;
}

function Input({ ...props }: InputProps) {
  return (
    <div className="w-full">
      <input
        className={`px-5 py-2 rounded-md bg-slate-200 w-full ${props.className}`}
        {...props}
      />
      {props.error && <small className="text-red-500">{props.error}</small>}
    </div>
  );
}

export default Input;
