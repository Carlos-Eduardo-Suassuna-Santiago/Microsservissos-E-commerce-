import { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem('token') || '');

  const [user, setUser] = useState(() => {
  const token = localStorage.getItem('token');
  const userId = localStorage.getItem('user_id');
  return { token, user_id: userId };
});

  const login = (token) => {
  const payload = JSON.parse(atob(token.split('.')[1]));
  localStorage.setItem('token', token);
  localStorage.setItem('user_id', payload.user_id);
  setUser({ token, user_id: payload.user_id });
};

  const logout = () => {
    localStorage.removeItem('token');
    setToken('');
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
