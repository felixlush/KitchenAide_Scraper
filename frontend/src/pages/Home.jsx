import React, { useState } from 'react';
import mixer from '../assets/mixer_logo.svg';

const Home = () => {
    const [prices, setPrices] = useState([]);
    const [errors, setErrors] = useState([]);
    const [loading, setLoading] = useState(false);

    const scrape = () => {
        setLoading(true);
        setPrices([]);
        setErrors([]);

        fetch("http://127.0.0.1:5000/api/scrape")
            .then((response) => response.json())
            .then((data) => {
                const { results, errors } = data;
                setPrices(results);
                setErrors(errors);
            })
            .catch((error) => {
                console.error("Error fetching scrape data:", error);
                setErrors([`Error fetching scrape data: ${error.message}`]);
            })
            .finally(() => {
                setLoading(false);
            });
    };

    return (
        <section>
            <div className="p-10 flex items-center justify-between">
                <div className="align-middle">
                    <h1 className="text-4xl font-bold tracking-wider mt-0 m-10 mb-0">KitchenAid</h1>
                    <h1 className="text-4xl font-bold tracking-wider mt-0 m-10 mb-0">WebScraper</h1>
                </div>
                <div className="flex justify-center">
                    <img src={mixer} alt="mixer" />
                </div>
            </div>

            <div className="flex justify-center p-5 mb-10">
                <button
                    className="bg-yellow-600 rounded-lg p-2 text-white font-bold hover:bg-amber-500"
                    onClick={scrape}
                    disabled={loading}
                >
                    {loading ? "Scraping..." : "Scrape"}
                </button>
            </div>

            {loading && (
                <div className="w-full bg-gray-200 rounded-full h-4 mb-4">
                    <div
                        className="bg-yellow-500 h-4 rounded-full"
                        style={{ width: "50%" }} // Simulate 50% progress
                    ></div>
                </div>
            )}

            {/* Display Errors */}
            {errors.length > 0 && (
                <div className="mt-6">
                    <h2 className="text-2xl font-bold mb-4">Errors</h2>
                    <ul className="text-red-600">
                        {errors.map((error, index) => (
                            <li key={index}>{error}</li>
                        ))}
                    </ul>
                </div>
            )}

            {/* Display Scraped Prices */}
            {prices.length > 0 && (
            <div className="flex flex-col">
                <div className="overflow-x-auto">
                    <div className="min-w-full inline-block align-middle">
                        <div className="overflow-hidden">
                            <table className="min-w-full divide-y divide-gray-200">
                                <thead>
                                    <tr>
                                        <th
                                            scope="col"
                                            className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                                        >
                                            Sku
                                        </th>
                                        <th
                                            scope="col"
                                            className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                                        >
                                            Name
                                        </th>
                                        <th
                                            scope="col"
                                            className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                                        >
                                            Company
                                        </th>
                                        <th
                                            scope="col"
                                            className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase "
                                        >
                                            Colour
                                        </th>
                                        <th
                                            scope="col"
                                            className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                                        >
                                            Price
                                        </th>
                                        <th
                                            scope="col"
                                            className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase "
                                        >
                                            URL
                                        </th>
                                    </tr>
                                </thead>
                                <tbody className="divide-y divide-gray-200">
                                    {prices.map((price, index) => (
                                        <tr key={index}>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800">
                                                {price.sku}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                                                {price.name}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-800 ">
                                                {price.company}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-800 ">
                                                {price.colour}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-800 ">
                                                {price.price}
                                            </td>
                                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-800 ">
                                                <a
                                                    href={price.url}
                                                    target="_blank"
                                                    rel="noopener noreferrer"
                                                    className="text-blue-600 hover:text-blue-800 dark:text-blue-500 dark:hover:text-blue-400"
                                                >
                                                    {price.url}
                                                </a>
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            )}
        </section>
    );
};

export default Home;
