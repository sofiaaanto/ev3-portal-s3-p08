import { useState, useEffect } from "react";
import "./global.css";
function App() {
  const [mensaje, setMensaje] = useState("");
  const [archivos, setArchivos] = useState([]);

  const [subiendo, setSubiendo] = useState(false);
  const [progreso, setProgreso] = useState(0);
  const [orden, setOrden] = useState({ campo: "fecha", direccion: "desc" });

  const toggleOrden = (campo) => {
    setOrden((prevOrden) => {
      const direccion =
        prevOrden.campo === campo && prevOrden.direccion === "asc"
          ? "desc"
          : "asc";
      return { campo, direccion };
    });
  };

  const archivosOrdenados = [...archivos].sort((a, b) => {
    if (orden.campo === "nombre") {
      return orden.direccion === "asc"
        ? a.nombre.localeCompare(b.nombre)
        : b.nombre.localeCompare(a.nombre);
    }
    if (orden.campo === "tamano") {
      return orden.direccion === "asc" ? a.tamano - b.tamano : b.tamano - a.tamano;
    }
    if (orden.campo === "fecha") {
      return orden.direccion === "asc"
        ? new Date(a.fecha) - new Date(b.fecha)
        : new Date(b.fecha) - new Date(a.fecha);
    }
    return 0;
  });

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
      setSubiendo(true);
      setProgreso(0);

      const uploadResponse = await new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();

        xhr.open("PUT", data.presignedUrl);

        xhr.setRequestHeader(
          "Content-Type",
          file.type
        );

        xhr.upload.onprogress = (event) => {
          if (event.lengthComputable) {
            const porcentaje = Math.round(
              (event.loaded * 100) / event.total
            );

            setProgreso(porcentaje);
          }
        };

        xhr.onload = () => {
          resolve({
            ok: xhr.status >= 200 && xhr.status < 300
          });
        };

        xhr.onerror = () => reject();

        xhr.send(file);
      });

      if (uploadResponse.ok) {
        setProgreso(100);
        setMensaje("");
        obtenerArchivos();

        setTimeout(() => {
          setSubiendo(false);
          setProgreso(0);
        }, 1000);
      } else {
        setMensaje("Error al subir archivo");
      }

    } catch (error) {
      console.error(error);
      setMensaje("Error");
      setSubiendo(false);
      setProgreso(0);
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
    <div className="app-container">
    <h1> Bucket para subir archivos 🍓</h1>

      <input
        type="file"
        accept=".docx,.pptx"
        onChange={handleFileChange}
      />

      <div className="orden-botones" style={{ margin: "1rem 0" }}>
        <button onClick={() => toggleOrden("nombre")}> 
          {orden.campo === "nombre" && orden.direccion === "asc" ? "Nombre Z-A" : "Nombre A-Z"}
        </button>

        <button onClick={() => toggleOrden("tamano")}> 
          {orden.campo === "tamano" && orden.direccion === "asc" ? "Tamaño ↓" : "Tamaño ↑"}
        </button>

        <button onClick={() => toggleOrden("fecha")}> 
          {orden.campo === "fecha" && orden.direccion === "asc" ? "Más antiguos" : "Más recientes"}
        </button>
      </div>

      {subiendo && (
        <div className="barra-container">
          <div
            className="barra-carga"
            style={{ width: `${progreso}%` }}
          ></div>
        </div>
      )}

      {subiendo && (
        <p>🍓 Subiendo archivo... {progreso}%</p>
      )}
      {mensaje && <p>{mensaje}</p>}

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
          {archivosOrdenados.map((archivo) => (
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