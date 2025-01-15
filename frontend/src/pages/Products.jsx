import React from 'react'
import { useState, useEffect } from 'react';
const Products = () => {
    const [name, setName] = useState("");
    const [url, setUrl] = useState("");
    const [company, setCompany] = useState("");
    const [productList, setProductList] = useState([]);
    const [companyList, setCompanyList] = useState([])

    useEffect(() => {
        fetch("http://127.0.0.1:5000/api/products")
        .then(response => response.json())
        .then(data => {
        setProductList(data);
        })
        .catch(error => {
        console.error("Error fecthing products from Flask API: ", error)
        })
    }, [])

    useEffect(() => {
        fetch("http://127.0.0.1:5000/api/companies")
        .then(response => response.json())
        .then(data => {
        setCompanyList(data);
        console.log("Fetched companies:", data);
        })
        .catch(error => {
        console.error("Error fetching companies from Flask API: ", error)
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
        <div className='p-10 ml-10 mr-10'>
            <h1 className="text-4xl font-bold tracking-wider mb-6">Products</h1>
            <div className="p-6 rounded-lg mb-5">
                <form onSubmit={handleAddProduct} className="space-y-6">
                {/* Product Name Field */}
                <div>
                    <label htmlFor="ProductName" className="block text-sm font-medium text-gray-700 mb-2">
                    Product Name
                    </label>
                    <input
                    type="text"
                    id="ProductName"
                    placeholder="Enter product name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-yellow-400 focus:outline-none"
                    />
                </div>

                {/* URL Field */}
                <div>
                    <label htmlFor="URL" className="block text-sm font-medium text-gray-700 mb-2">
                    URL
                    </label>
                    <input
                    type="url"
                    id="URL"
                    placeholder="Enter product URL"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-yellow-400 focus:outline-none"
                    />
                </div>

                {/* Company Field */}
                <div>
                    <label htmlFor="Company" className="block text-sm font-medium text-gray-700 mb-2">
                    Company
                    </label>
                    <select
                    id="Company"
                    value={company}
                    onChange={(e) => setCompany(e.target.value)}
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-yellow-400 focus:outline-none"
                    >
                    <option value="" disabled>
                        --- Choose A Company ---
                    </option>
                    {companyList.map((company) => (
                        <option value={company.name} key={company.id}>
                            {company.name}
                        </option>
                    ))}
                    </select>
                </div>

                {/* Submit Button */}
                <button
                    type="submit"
                    className="w-full sm:w-auto px-4 py-3 text-white bg-yellow-600 hover:bg-yellow-500 font-bold rounded-lg focus:ring-4 focus:ring-yellow-300 focus:outline-none"
                >
                    Add Product
                </button>
                </form>
            </div>
            <h3 className='text-2xl font-bold tracking-wider'>Current Products</h3>
            <div className="mt-5">
                <table className="table-auto w-full border-collapse border overflow-scroll">
                    <thead>
                    <tr className="bg-yellow-600 text-white text-left">
                        <th className="px-4 py-2 border">Product Name</th>
                        <th className="px-4 py-2 border">Company</th>
                        <th className="px-4 py-2 border">URL</th>
                    </tr>
                    </thead>
                    <tbody>
                    {productList.map((p, i) => (
                        <tr key={p.id} className={`hover:bg-blue-50 ${i % 2 === 0 ? 'bg-white' : 'bg-blue-50'}`}>
                        <td className="px-4 py-2 border">{p.name}</td>
                        <td className="px-4 py-2 border">{p.company}</td>
                        <td className="px-4 py-2 border">
                            <a href={p.url} className="text-blue-600 underline hover:text-blue-800">
                            {p.url}
                            </a>
                        </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}

export default Products