import React from "react";
import Button from "../components/button";
import Input from "../components/input";
import { CommandIcon } from "lucide-react";
import instance from "../libs/axios-config";
import { useNavigate } from "react-router-dom";

function RegisterPage() {
  // Form states
  const [email, setEmail] = React.useState<string>("");
  const [password, setPassword] = React.useState<string>("");
  const [confirmPassword, setConfirmPassword] = React.useState<string>("");

  // Form error states
  const [emailError, setEmailError] = React.useState<string>("");
  const [passwordError, setPasswordError] = React.useState<string>("");
  const [confirmPasswordError, setConfirmPasswordError] =
    React.useState<string>("");

  // Loading state
  const [loading, setLoading] = React.useState<boolean>(false);

  // Navigation state
  const navigate = useNavigate();

  function handleEmail(e: React.ChangeEvent<HTMLInputElement>) {
    setEmail(e.target.value);

    if (!isValidEmail(e.target.value)) {
      setEmailError("Invalid email");
    } else {
      setEmailError("");
    }
  }

  function handlePassword(e: React.ChangeEvent<HTMLInputElement>) {
    setPassword(e.target.value);

    if (!isValidPassword(e.target.value)) {
      setPasswordError("Password must be at least 8 characters long");
    } else {
      setPasswordError("");
    }
  }

  function handleConfirmPassword(e: React.ChangeEvent<HTMLInputElement>) {
    setConfirmPassword(e.target.value);

    if (e.target.value !== password) {
      setConfirmPasswordError("Password does not match");
    } else {
      setConfirmPasswordError("");
    }
  }

  function isValidEmail(email: string) {
    return /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);
  }

  function isValidPassword(password: string) {
    return /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(
      password,
    );
  }

  async function handleForm(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setLoading(true);

    try {
      await instance.post("/auth/register", {
        email,
        password,
      });

      // reroute to login page
      navigate("/login");
    } catch (error: any) {
      if (error.response && error.response.status === 409) {
        setEmailError("Email already exists");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex flex-col items-center justify-center py-20 max-w-screen-lg mx-auto w-11/12 gap-5">
      {/* Header */}
      <div className="flex flex-col items-center">
        <CommandIcon size={30} />
        <h1 className="font-bold text-xl">Sign Up Here</h1>
        <p className="text-slate-500">Enter your email to create account.</p>
      </div>

      {/* Form content */}
      <form
        className="flex flex-col items-center mx-auto w-[300px] gap-2"
        onSubmit={handleForm}
      >
        <Input
          placeholder="name@example.com"
          type="email"
          value={email}
          onChange={handleEmail}
          error={emailError}
        />

        <Input
          placeholder="Password"
          type="password"
          value={password}
          onChange={handlePassword}
          error={passwordError}
        />

        <Input
          placeholder="Confirm Password"
          type="password"
          value={confirmPassword}
          onChange={handleConfirmPassword}
          error={confirmPasswordError}
        />

        <Button type="submit">Sign Up With Email</Button>
      </form>

      {/* Footer */}
    </div>
  );
}

export default RegisterPage;
