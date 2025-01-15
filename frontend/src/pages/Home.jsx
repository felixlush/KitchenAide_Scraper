import React, { useState } from 'react'
import mixer from '../assets/mixer_logo.svg'

const Home = () => {

    const [prices, setPrices] = useState([])
    const [hasScraped, setHasScraped] = useState(false)
    const [loading, setLoading] = useState(false);

    const scrape = () => {
        setLoading(true)
        fetch("http://127.0.0.1:5000/api/scrape")
        .then(response => response.json())
        .then(data => {
            setPrices(data);
            setHasScraped(true);
        })
        .catch(error => {
            console.error("Error fetching prices from Flask API: ", error)
        })
        .finally(() => {
            setLoading(false)
        })
    }

    return (
        <section>
            <div className='p-10 flex items-center justify-between'>
                <div className='align-middle'>
                    <h1 className='text-4xl font-bold tracking-wider mt-0 m-10 mb-0'>KitchenAid</h1>
                    <h1 className='text-4xl font-bold tracking-wider mt-0 m-10 mb-0'>WebScraper</h1>
                </div>
                <div className='flex justify-center'>
                    <img src={mixer} alt="mixer"/>
                </div>
            </div>
            <div className='flex justify-center p-5 mb-10'>
                <button
                className='bg-yellow-600 rounded-lg p-2 text-white font-bold hover:bg-amber-500'
                onClick={scrape}
                disabled={loading} // Disable button while loading
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


            {hasScraped && !loading && (
                <div>
                    <table>
                        <thead>
                            <tr>
                                <th>Product Name</th>
                                <th>Price</th>
                                <th>Company</th>
                                <th>URL</th>
                            </tr>
                        </thead>
                        <tbody>
                            {prices.map((price) => {
                                <tr>
                                    <td>{price.name}</td>
                                    <td>{price.price}</td>
                                    <td>{price.company}</td>
                                    <td>{price.url}</td>
                                </tr>
                            })}
                        </tbody>
                    </table>
                </div>
            )}
        </section>
    )
}

export default Home