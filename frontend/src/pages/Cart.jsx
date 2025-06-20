// src/pages/Cart.jsx
import { useEffect, useState } from 'react';
import api from '../api/api';
import { useAuth } from '../auth/AuthContext';
import { Link } from 'react-router-dom';

export default function Cart() {
  const { token, user_id } = useAuth();
  const [cart, setCart] = useState([]);

  const headers = { Authorization: `Bearer ${token}` };

  useEffect(() => {
    fetchCart();
  }, []);

  const fetchCart = async () => {
    const res = await api.get(`/cart/${user_id}`, { headers });
    setCart(res.data);
  };

  const removeItem = async (itemId) => {
    await api.delete(`/cart/${itemId}`, { headers });
    fetchCart();
  };

  const updateQuantity = async (itemId, quantity) => {
    if (quantity < 1) return;
    await api.put(`/cart/${itemId}`, { quantity }, { headers });
    fetchCart();
  };

  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  return (
    <div>
      <h2>Seu Carrinho</h2>
      {cart.length === 0 ? <p>Seu carrinho está vazio.</p> : (
        <table>
          <thead>
            <tr>
              <th>Produto</th>
              <th>Preço</th>
              <th>Qtd</th>
              <th>Total</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {cart.map(item => (
              <tr key={item.id}>
                <td>{item.product_name}</td>
                <td>R$ {item.price}</td>
                <td>
                  <input
                    type="number"
                    value={item.quantity}
                    min={1}
                    onChange={(e) => updateQuantity(item.id, parseInt(e.target.value))}
                  />
                </td>
                <td>R$ {(item.price * item.quantity).toFixed(2)}</td>
                <td>
                  <button onClick={() => removeItem(item.id)}>Remover</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      <h3>Total: R$ {total.toFixed(2)}</h3>
      <Link to="/checkout">
        <button>Finalizar Pedido</button>
      </Link>
    </div>
  );
}
