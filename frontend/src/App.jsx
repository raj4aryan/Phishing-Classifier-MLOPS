import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState("");

  const handlePredict = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const formData = new FormData();
      formData.append("file", file);

      const response = await axios.post(
        "http://localhost:8000/predict",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResponseData(response.data);
    } catch (err) {
      console.error(err);
      setError("Prediction failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Network Security Classifier</h1>

      <div className="upload-section">
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button onClick={handlePredict}>
          {loading ? "Predicting..." : "Predict"}
        </button>
      </div>

      {error && <p className="error">{error}</p>}

      {responseData && (
        <>
          <div className="summary-container">
            <div className="card">
              <h3>Total Records</h3>
              <p>{responseData.total_records}</p>
            </div>

            <div className="card">
              <h3>Legitimate</h3>
              <p>{responseData.legitimate_count}</p>
            </div>

            <div className="card">
              <h3>Phishing</h3>
              <p>{responseData.phishing_count}</p>
            </div>
          </div>

          <table>
            <thead>
              <tr>
                <th>#</th>
                <th>Prediction</th>
                <th>Confidence</th>
              </tr>
            </thead>

            <tbody>
              {responseData.results.map((item, index) => (
                <tr key={index}>
                  <td>{index + 1}</td>

                  <td
                    className={
                      item.prediction === "Legitimate"
                        ? "legitimate"
                        : "phishing"
                    }
                  >
                    {item.prediction}
                  </td>

                  <td>{item.confidence}%</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
}

export default App;