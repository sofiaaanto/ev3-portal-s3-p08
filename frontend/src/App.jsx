import { useState } from "react";

function App() {

  const [mensaje, setMensaje] = useState("");

  const uploadFile = async (file) => {

    try {

      // Solicitar URL firmada
      const response = await fetch(
        "http://127.0.0.1:8000/api/upload/presigned-url",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            fileName: file.name,
            fileType: file.type,
            fileSize: file.size
          })
        }
      );

      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      // Subir archivo a S3
      const uploadResponse = await fetch(
        data.presignedUrl,
        {
          method: "PUT",
          headers: {
            "Content-Type": file.type
          },
          body: file
        }
      );

      if (uploadResponse.ok) {
        setMensaje("Archivo subido correctamente");
      } else {
        setMensaje("Error al subir archivo");
      }

    } catch (error) {
      console.error(error);
      setMensaje("Error");
    }
  };

  const handleFileChange = async (event) => {

    const file = event.target.files[0];

    if (!file) return;

    await uploadFile(file);
  };

  return (
    <div>
      <h1>Subida de archivos</h1>

      <input
        type="file"
        accept=".docx,.pptx"
        onChange={handleFileChange}
      />

      <p>{mensaje}</p>
    </div>
  );
}

export default App;