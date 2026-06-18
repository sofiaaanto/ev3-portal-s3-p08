import { useState, useEffect } from "react";

function App() {

  const [mensaje, setMensaje] = useState("");
  const [archivos, setArchivos] = useState([]);

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
        obtenerArchivos();
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

  const obtenerArchivos = async () => {

    const response = await fetch(
      "http://127.0.0.1:8000/api/files"
    );

    const data = await response.json();

    setArchivos(data);
  };

  const eliminarArchivo = async (id) => {

    const response = await fetch(
      `http://127.0.0.1:8000/api/files/${id}`,
      {
        method: "DELETE"
      }
    );

    if (response.ok) {
      obtenerArchivos();
    }
  };

  useEffect(() => {
    obtenerArchivos();
  }, []);

  return (
    <div>
      <h1>Subida de archivos</h1>

      <input
        type="file"
        accept=".docx,.pptx"
        onChange={handleFileChange}
      />

      <p>{mensaje}</p>

      <h2>Archivos en S3</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Tamaño (KB)</th>
            <th>Fecha</th>
            <th>Acción</th>
          </tr>
        </thead>

        <tbody>
          {archivos.map((archivo) => (
            <tr key={archivo.id}>
              <td>{archivo.nombre}</td>

              <td>
                {(archivo.tamano / 1024).toFixed(2)}
              </td>

              <td>
                {new Date(
                  archivo.fecha
                ).toLocaleString()}
              </td>

              <td>
                <button
                  onClick={() =>
                    eliminarArchivo(archivo.id)
                  }
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;