import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../auth/AuthContext';

export default function Header() {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1rem', background: '#282c34', color: '#fff' }}>
      <nav style={{ display: 'flex', gap: '1rem' }}>
        <Link to="/products" style={{ color: '#fff', textDecoration: 'none' }}>Produtos</Link>
        <Link to="/cart" style={{ color: '#fff', textDecoration: 'none' }}>Carrinho</Link>
        <Link to="/checkout" style={{ color: '#fff', textDecoration: 'none' }}>Checkout</Link>
        <Link to="/orders" style={{ color: '#fff', textDecoration: 'none' }}>Pedidos</Link>
      </nav>
      <button onClick={handleLogout} style={{ background: 'red', color: '#fff', border: 'none', padding: '0.5rem 1rem', cursor: 'pointer' }}>
        Sair
      </button>
    </header>
  );
}
