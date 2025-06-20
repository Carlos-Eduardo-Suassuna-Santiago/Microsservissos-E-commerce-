import { useEffect, useState } from 'react';
import api from '../api/api';
import { useAuth } from '../auth/AuthContext';

export default function Orders() {
  const { token, user_id } = useAuth();
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  const headers = { Authorization: `Bearer ${token}` };

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const res = await api.get(`/orders/${user_id}`, { headers });
        setOrders(res.data);
      } catch (err) {
        console.error("Erro ao buscar pedidos", err);
      } finally {
        setLoading(false);
      }
    };

    fetchOrders();
  }, [user_id]);

  if (loading) return <p>Carregando pedidos...</p>;

  if (orders.length === 0) return <p>Você não possui pedidos.</p>;

  return (
    <div>
      <h2>Histórico de Pedidos</h2>
      {orders.map(order => (
        <div key={order.id} style={{ border: '1px solid #ccc', marginBottom: '1rem', padding: '1rem' }}>
          <p><strong>ID do pedido:</strong> {order.id}</p>
          <p><strong>Data:</strong> {new Date(order.created_at).toLocaleString()}</p>
          <p><strong>Status:</strong> {order.status}</p>
          <table>
            <thead>
              <tr>
                <th>Produto</th>
                <th>Qtd</th>
                <th>Preço Unit.</th>
                <th>Total</th>
              </tr>
            </thead>
            <tbody>
              {order.items.map(item => (
                <tr key={item.product_id}>
                  <td>{item.product_name}</td>
                  <td>{item.quantity}</td>
                  <td>R$ {item.price.toFixed(2)}</td>
                  <td>R$ {(item.price * item.quantity).toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <p><strong>Total do pedido: </strong> R$ {order.total.toFixed(2)}</p>
        </div>
      ))}
    </div>
  );
}
