import React from 'react'
import { useState, useEffect } from 'react';
import ProductsCard from '../components/ProductsCard';
const Products = () => {
    const [name, setName] = useState("");
    const [sku, setSku] = useState("");
    const [colour, setColour] = useState("");
    const [url, setUrl] = useState("");
    const [company, setCompany] = useState("");
    const [productList, setProductList] = useState([]);
    const [filteredProducts, setFilteredProducts] = useState([]);
    const [companyList, setCompanyList] = useState([])
    const [searchTerm, setSearchTerm] = useState("");
    const [filterTerm, setFilterTerm] = useState([]);

    const handleFilterChange = (e) => {
        setFilterTerm(e.target.value);
    }

    const handleSearchChange = (e) => {
        setSearchTerm(e.target.value);
    }


    useEffect(() => {
        fetch(`http://127.0.0.1:5000/api/products?search=${encodeURIComponent(searchTerm)}&filter=${encodeURIComponent(filterTerm)}`)
        .then((response) => response.json())
        .then((data) => {
            setProductList(data);
        })
        .catch((error) => {
            console.error("Error fetching filtered products from Flask API: ", error);
        });
    }, [searchTerm, filterTerm]);

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

    const refreshProducts = () => {
        fetch("http://127.0.0.1:5000/api/products")
        .then(response => response.json())
        .then(data => {
        setProductList(data);
        })
        .catch(error => {
        console.error("Error fecthing products from Flask API: ", error)
        })
    }


    const handleAddProduct = (e) => {
        e.preventDefault();
        fetch("http://127.0.0.1:5000/api/products", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, url, company, sku, colour }),
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
                <div>
                    <label htmlFor="ProductSku" className="block text-sm font-medium text-gray-700 mb-2">
                    Product Sku
                    </label>
                    <input
                    type="text"
                    id="ProductSku"
                    placeholder="Enter sku"
                    value={sku}
                    onChange={(e) => setSku(e.target.value)}
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-yellow-400 focus:outline-none"
                    />
                </div>
                {/* Product Name Field */}
                <div>
                    <label htmlFor="ProductName" className="block text-sm font-medium text-gray-700 mb-2">
                    Product Name
                    </label>
                    <input
                    type="text"
                    id="ProductName"
                    placeholder="Enter name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-yellow-400 focus:outline-none"
                    />
                </div>
                <div>
                    <label htmlFor="ProductColour" className="block text-sm font-medium text-gray-700 mb-2">
                    Product Colour
                    </label>
                    <input
                    type="text"
                    id="ProductColour"
                    placeholder="Enter colour"
                    value={colour}
                    onChange={(e) => setColour(e.target.value)}
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
                    placeholder="Enter URL"
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
            {/* Search and Filter Section */}
            <div className="flex gap-4 mb-6 ml-10 mr-10 mt-5">
                {/* Search Input */}
                <input
                    type="text"
                    placeholder="Search by sku"
                    value={searchTerm}
                    onChange={handleSearchChange}
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-yellow-400 focus:outline-none"
                />

                {/* Filter Dropdown */}
                <select
                    value={filterTerm}
                    onChange={handleFilterChange}
                    className="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-yellow-400 focus:outline-none"
                >
                    <option value="">--- Filter by Company ---</option>
                    {companyList.map((company) => (
                        <option value={company.name} key={company.id}>
                            {company.name}
                        </option>
                    ))}
                </select>
            </div>
            <div className="mt-5">
                <ProductsCard productList={productList} refreshProducts={refreshProducts}/>
            </div>
            
        </div>
    )
}

export default Products