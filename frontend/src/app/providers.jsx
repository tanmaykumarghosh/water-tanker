import { BrowserRouter } from "react-router-dom";

import AuthProvider from "../context/AuthContext";

export default function Providers({ children }) {
    return (
        
            <AuthProvider>
                {children}
            </AuthProvider>
       
    );
}