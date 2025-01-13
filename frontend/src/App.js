import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from 'react'

function App() {
  const [name, setName] = useState("");
  const [url, setUrl] = useState("");
  const [company, setCompany] = useState("");
  const [productList, setProductList] = useState([]);
  const[msg, setMsg] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/products")
    .then(response => response.json())
    .then(data => {
      setProductList(data);
    })
    .catch(error => {
      console.error("Error fecthing from Flask API: ", error)
    })
  }, [])

  const handleAddProduct = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:5000/api/products", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, url, company }),
    })
      .then(res => res.json())
      .then(() => {
        setName("");
        setUrl("");
        setCompany("");
        // Reload product list
        return fetch("http://127.0.0.1:5000/api/products");
      })
      .then(res => res.json())
      .then(data => setProductList(data))
      .catch(err => console.error(err));
  };


  return (
    <div className='p-10'>
      <h1 className='text-3xl p-5 text-center'>Products</h1>
      <div className='p-6 text-center outline-4'>
        <form onSubmit={handleAddProduct}>
          <input
            placeholder="Product Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <input
            placeholder="URL"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
          />
          <input
            placeholder="Company"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
          />
          <button type="submit">Add Product</button>
        </form>
      </div>
      <h3 className='text-xl font-semibold'>Current Products</h3>
      <div className='mt-5 bg-blue-200 rounded-lg p-4 justify-between'>
        <table className='table-auto'>
          <thead>
            <tr>
              <th>Product ID</th>
              <th>Company</th>
              <th>URL</th>
            </tr>
          </thead>
          <tbody>
            {productList.map((p, i) => (
              <tr key={i}>
                <td>
                  {p.name}
                </td>
                <td>
                  {p.company}
                </td>
                <td>
                  {p.url}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
export default App;
