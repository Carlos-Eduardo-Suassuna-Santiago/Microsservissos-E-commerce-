import Header from './Header';

export default function Layout({ children }) {
  return (
    <>
      <Header />
      <main style={{ padding: '1rem' }}>
        {children}
      </main>
    </>
  );
}
