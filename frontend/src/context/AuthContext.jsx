import { createContext, useEffect, useState } from "react";

import { getProfile, login as loginApi } from "../features/accounts/api/auth";

export const AuthContext = createContext();

export default function AuthProvider({ children }) {

    const [user, setUser] = useState(null);

    const [loading, setLoading] = useState(true);

  useEffect(() => {

    console.log(
        "AUTH STATE",
        {
            user,
            loading
        }
    );

}, [user, loading]);

    const loadUser = async () => {

        const token = localStorage.getItem("access");

        if (!token) {

            setLoading(false);

            return;
        }

        try {

            const response = await getProfile();

            setUser(response.data.data);

        } catch (error) {

            console.error(error);

            logout();

        }

        setLoading(false);
    };

    const login = async (phone, password) => {

        const response = await loginApi({
            phone,
            password,
        });

        const data = response.data.data;

        localStorage.setItem(
            "access",
            data.access
        );

        localStorage.setItem(
            "refresh",
            data.refresh
        );

        setUser(data.user);

        return data.user;
    };

   const logout = async () => {

        try {

            await logoutApi({
                refresh: localStorage.getItem("refresh"),
            });

        } catch (error) {

            console.error(error);

        } finally {

            localStorage.removeItem("access");

            localStorage.removeItem("refresh");

            localStorage.removeItem("user");

            setUser(null);

        }

    };

    return (

        <AuthContext.Provider
            value={{
                user,
                loading,
                login,
                logout,
                loadUser,
                isAuthenticated: !!user,
            }}
        >

            {children}

        </AuthContext.Provider>

    );
}