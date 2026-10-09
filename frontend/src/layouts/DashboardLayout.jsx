import { Link, Outlet, useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";
export default function DashboardLayout() {
    
    const navigate = useNavigate();

    const { logout, user } = useAuth();

    const handleLogout = () => {

        logout();

        navigate("/login", {
            replace: true,
        });

    };
    const menus = {
        CUSTOMER: [
            { label: "Dashboard", to: "/customer" },
            // { label: "My Requests", to: "/customer/requests" },
            { label: "New Request", to: "/instant-request" },
            // { label: "Quotations", to: "/customer/quotations" },
        ],

        DRIVER: [
            { label: "Dashboard", to: "/driver" },
            // { label: "Inbox", to: "/driver/requests" },
            { label: "Active Job", to: "/driver/jobs" },
            { label: "Job History", to: "/driver/jobs/history" },
            // { label: "My Tankers", to: "/driver/tankers" },
        ],

        PROVIDER: [
            { label: "Dashboard", to: "/provider" },
            { label: "Requests", to: "/provider/requests" },
            { label: "Quotations", to: "/provider/quotations" },
            { label: "Tankers", to: "/provider/tankers" },
        ],
    };

    const roleMenus = menus[user?.role] || [];
    return (
        <div
            style={{
                display: "flex",
            }}
        >
            <aside
                style={{
                    width: "220px",
                    borderRight: "1px solid #ddd",
                    minHeight: "100vh",
                    padding: "20px",
                }}
            >
                <h3>Dashboard</h3>

                <p>
                    <Link to="/">Home</Link>
                </p>
                <h4>
                    {user?.first_name}
                </h4>

                {/* your menu */}


                {roleMenus.map((item) => (
                    <p key={item.to}>
                        <Link to={item.to}>
                            {item.label}
                        </Link>
                    </p>
                ))}
                <button
                    className="btn btn-danger w-100 mt-4"
                    onClick={handleLogout}
                >
                    Logout
                </button>
            </aside>

            <main
                style={{
                    flex: 1,
                    padding: "30px",
                }}
            >
                <Outlet />
            </main>
        </div>
    );
}