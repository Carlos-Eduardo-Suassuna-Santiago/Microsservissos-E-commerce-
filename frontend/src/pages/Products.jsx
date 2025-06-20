import { useEffect, useState } from 'react';
import api from '../api/api';
import { useAuth } from '../auth/AuthContext';

export default function Products() {
  const [products, setProducts] = useState([]);
  const { token } = useAuth();

  useEffect(() => {
    api.get('/products').then(res => setProducts(res.data));
  }, []);

  const addToCart = async (productId) => {
    await api.post('/cart', { product_id: productId, quantity: 1 }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    alert('Produto adicionado ao carrinho!');
  };

  return (
    <div>
      <h2>Produtos</h2>
      <ul>
        {products.map(p => (
          <li key={p.id}>
            {p.name} - R${p.price}
            <button onClick={() => addToCart(p.id)}>Adicionar</button>
            
          </li>
        ))}
      </ul>
      <a href="/cart">Ver Carrinho</a>
      <br />
      <a href="/orders">Meus Pedidos</a>
    </div>
  );
}
