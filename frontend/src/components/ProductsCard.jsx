import React from 'react'
import { useState, useEffect } from 'react';

const ProductsCard = ({productList, refreshProducts}) => {

    const [editPanelOpen, setEditPanelOpen] = useState(false);
    const [selectedItem, setSelectedItem] = useState();
    const [id, setId] = useState("");
    const [name, setName] = useState("");
    const [sku, setSku] = useState("");
    const [colour, setColour] = useState("");
    const [url, setUrl] = useState("");
    const [company, setCompany] = useState("");

    const handleEditClick = (product) => {
        setSelectedItem(product)
        setName(product.name)
        setColour(product.colour)
        setSku(product.sku)
        setUrl(product.url)
        setId(product.id)
        setCompany(product.company)
        setEditPanelOpen(true)
    }

    const closeEditPanel = () => {
        setSelectedItem()
        setEditPanelOpen(false)
    }

    const updateProduct = (e) => {
        e.preventDefault();

        fetch(`http://127.0.0.1:5000/api/products/update`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(selectedItem),
        })
        .then(
            response => response.json()
        )
        .then(() => {
            refreshProducts()
            closeEditPanel()
        })
        .catch(error => {
            console.error("Error update product", error)
        })
    }

    return (
        <section>
            <div>
                <table className="table-auto w-full border-collapse border overflow-scroll">
                        <thead>
                        <tr className="bg-yellow-600 text-white text-left">
                            <th className="px-4 py-2 border">Sku</th>
                            <th className="px-4 py-2 border">Product Name</th>
                            <th className="px-4 py-2 border">Colour</th>
                            <th className="px-4 py-2 border">Company</th>
                            <th className="px-4 py-2 border">URL</th>
                            <th className="px-4 py-2 border">Update</th>
                        </tr>
                        </thead>
                        <tbody>
                        {productList.map((p, i) => (
                            <tr key={p.id} className={`hover:bg-blue-50 ${i % 2 === 0 ? 'bg-white' : 'bg-blue-50'}`}>
                            <td className="px-4 py-2 border">{p.sku}</td>
                            <td className="px-4 py-2 border">{p.name}</td>
                            <td className="px-4 py-2 border">{p.colour}</td>
                            <td className="px-4 py-2 border">{p.company}</td>
                            <td className="px-4 py-2 border">
                                <a href={p.url} className="text-blue-600 underline hover:text-blue-800">
                                {p.url}
                                </a>
                            </td>
                            <td className="px-4 py-2 border"><button className='bg-green-700 rounded-md p-2 text-white font-bold' onClick={() => handleEditClick(p)}>Edit</button></td>
                            </tr>
                        ))}
                        </tbody>
                </table>
            </div>

            {editPanelOpen && selectedItem && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
                    <div className="bg-white p-6 rounded-lg shadow-lg w-1/3">
                        <div className='flex'>
                        <h2 className="text-2xl font-bold mb-4 mr-auto">Edit Product</h2>
                        <p className='text-gray-400'>Item ID: {selectedItem.id}</p>
                        </div>
                        <form onSubmit={(e) => updateProduct(e)}>
                            <div className="mb-4">
                                <label className="block text-gray-700">Sku</label>
                                <input
                                    type="text"
                                    value={selectedItem.sku}
                                    onChange={(e) => setSelectedItem({ ...selectedItem, sku: e.target.value })}
                                    className="border rounded-lg p-2 w-full"
                                />
                            </div>
                            <div className="mb-4">
                                <label className="block text-gray-700">Name</label>
                                <input
                                    type='text'
                                    value={selectedItem.name}
                                    onChange={(e) => setSelectedItem({ ...selectedItem, name: e.target.value })}
                                    className="border rounded-lg p-2 w-full"
                                />
                            </div>
                            <div className="mb-4">
                                <label className="block text-gray-700">Colour</label>
                                <input
                                    type="text"
                                    value={selectedItem.colour}
                                    onChange={(e) => setSelectedItem({ ...selectedItem, colour: e.target.value })}
                                    className="border rounded-lg p-2 w-full"
                                />
                            </div>
                            <div className="mb-4">
                                <label className="block text-gray-700">Company</label>
                                <input
                                    value={selectedItem.company}
                                    onChange={(e) => setSelectedItem({ ...selectedItem, company: e.target.value })}
                                    className="border rounded-lg p-2 w-full"
                                />
                            </div>
                            <div className="mb-4">
                                <label className="block text-gray-700">URL</label>
                                <input
                                    type='text'
                                    value={selectedItem.url}
                                    onChange={(e) => setSelectedItem({ ...selectedItem, url: e.target.value })}
                                    className="border rounded-lg p-2 w-full"
                                />
                            </div>
                            <div className="flex justify-end space-x-4">
                                <button type="button" onClick={closeEditPanel} className="bg-gray-500 text-white px-4 py-2 rounded-lg">Cancel</button>
                                <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded-lg">Save Changes</button>
                            </div>
                        </form>
                    </div>
                </div>
            )}
        </section>
    )
}

export default ProductsCard