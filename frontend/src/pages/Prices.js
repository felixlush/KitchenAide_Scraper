import React from 'react'

const Prices = () => {

    const [priceList, setPriceList] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:5000/api/scrape")
        .then(response => response.json())
        .then(data => {
        setPriceList(data);
        })
        .catch(error => {
        console.error("Error fecthing from Flask API: ", error)
        })
    }, [])  

    return (
        <div>Prices</div>
    )
}

export default Prices