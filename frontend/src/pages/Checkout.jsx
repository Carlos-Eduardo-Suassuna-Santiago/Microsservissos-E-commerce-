// src/pages/Checkout.jsx
import { useEffect, useState } from 'react';
import api from '../api/api';
import { useAuth } from '../auth/AuthContext';
import { useNavigate } from 'react-router-dom';

export default function Checkout() {
  const { token, user_id } = useAuth();
  const [cart, setCart] = useState([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const headers = { Authorization: `Bearer ${token}` };

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    try {
      const res = await api.get(`/cart/${user_id}`, { headers });
      setCart(res.data);
    } catch (error) {
      console.error("Erro ao buscar carrinho", error);
    }
  };

  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  const handleConfirmOrder = async () => {
    if (cart.length === 0) {
      alert("Seu carrinho está vazio!");
      return;
    }
    setLoading(true);

    const orderData = {
      user_id,
      items: cart.map(item => ({
        product_id: item.product_id,
        quantity: item.quantity,
        price: item.price
      }))
    };

    try {
      await api.post('/orders', orderData, { headers });
      alert("Pedido realizado com sucesso!");
      navigate('/orders'); // Página de histórico de pedidos (você pode criar depois)
    } catch (error) {
      alert("Erro ao finalizar pedido.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Finalizar Pedido</h2>
      {cart.length === 0 ? (
        <p>Seu carrinho está vazio.</p>
      ) : (
        <>
          <table>
            <thead>
              <tr>
                <th>Produto</th>
                <th>Preço Unit.</th>
                <th>Quantidade</th>
                <th>Total</th>
              </tr>
            </thead>
            <tbody>
              {cart.map(item => (
                <tr key={item.id}>
                  <td>{item.product_name}</td>
                  <td>R$ {item.price.toFixed(2)}</td>
                  <td>{item.quantity}</td>
                  <td>R$ {(item.price * item.quantity).toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <h3>Total: R$ {total.toFixed(2)}</h3>
          <button onClick={handleConfirmOrder} disabled={loading}>
            {loading ? 'Processando...' : 'Confirmar Pedido'}
          </button>
        </>
      )}
    </div>
  );
}
