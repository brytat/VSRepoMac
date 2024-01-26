import React from "react";

type ThemeContextType = {
  theme: string;
  setTheme: React.Dispatch<React.SetStateAction<string>>;
};

export const ThemeContext = React.createContext({} as ThemeContextType);

interface ThemeProviderProps {
  children: React.ReactNode; // ReactNode == any valid TSX
}

function ThemeProvider(props: ThemeProviderProps) {
  // setting and getting the theme
  const [theme, setTheme] = React.useState("light");

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {props.children}
    </ThemeContext.Provider>
  );
}

export default ThemeProvider;
