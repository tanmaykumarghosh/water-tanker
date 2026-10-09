import React from "react";

export default function RequestForm({
    formData,
    countries,
    provinces,
    districts,
    capacities,
    loading,
    onChange,
    onSubmit,
    onUseCurrentLocation,
}) {
    return (
        <form onSubmit={onSubmit}>

            <h2>Instant Water Request</h2>

            <hr />

            <h3>Customer Information</h3>

            <div>
                <label>First Name</label>
                <br />
                <input
                    type="text"
                    name="first_name"
                    value={formData.first_name}
                    onChange={onChange}
                    required
                />
            </div>

            <br />

            <div>
                <label>Phone Number</label>
                <br />
                <input
                    type="text"
                    name="phone"
                    value={formData.phone}
                    onChange={onChange}
                    required
                />
            </div>

            <hr />

            <h3>Service Information</h3>

            <div>
                <label>Service Type</label>
                <br />

                <select
                    name="service_type"
                    value={formData.service_type}
                    onChange={onChange}
                >
                    <option value="WATER">
                        Water
                    </option>

                    <option value="SEPTIC">
                        Septic
                    </option>
                </select>
            </div>

            <br />

            <div>
                <label>Fulfillment</label>
                <br />

                <select
                    name="fulfillment_type"
                    value={formData.fulfillment_type}
                    onChange={onChange}
                >
                    <option value="SINGLE_DRIVER">
                        Single Driver
                    </option>

                    <option value="MULTIPLE_DRIVERS">
                        Multiple Drivers
                    </option>
                </select>
            </div>

            <br />

            <div>
                <label>Capacity</label>
                <br />

                <select
                    name="capacity_id"
                    value={formData.capacity_id}
                    onChange={onChange}
                    required
                >
                    <option value="">
                        Select Capacity
                    </option>

                    {capacities.map((item) => (
                        <option
                            key={item.id}
                            value={item.id}
                        >
                            {item.display_name}
                        </option>
                    ))}
                </select>
            </div>

            <br />

            <div>
                <label>Number of Tankers</label>
                <br />

                <input
                    type="number"
                    min="1"
                    name="number_of_tankers"
                    value={formData.number_of_tankers}
                    onChange={onChange}
                />
            </div>

            <br />

            <div>
                <label>Budget</label>
                <br />

                <input
                    type="number"
                    name="budget_amount"
                    value={formData.budget_amount}
                    onChange={onChange}
                />
            </div>

            <hr />

            <h3>Delivery Location</h3>

            <div>

                <label>Country</label>

                <br />

                <select
                    name="country_id"
                    value={formData.country_id}
                    onChange={onChange}
                    required
                >
                    <option value="">
                        Select Country
                    </option>

                    {countries.map((item) => (
                        <option
                            key={item.id}
                            value={item.id}
                        >
                            {item.name}
                        </option>
                    ))}
                </select>

            </div>

            <br />

            <div>

                <label>Province</label>

                <br />

                <select
                    name="province_id"
                    value={formData.province_id}
                    onChange={onChange}
                    required
                >
                    <option value="">
                        Select Province
                    </option>

                    {provinces.map((item) => (
                        <option
                            key={item.id}
                            value={item.id}
                        >
                            {item.name}
                        </option>
                    ))}
                </select>

            </div>

            <br />

            <div>

                <label>District</label>

                <br />

                <select
                    name="district_id"
                    value={formData.district_id}
                    onChange={onChange}
                >
                    <option value="">
                        Select District
                    </option>

                    {districts.map((item) => (
                        <option
                            key={item.id}
                            value={item.id}
                        >
                            {item.name}
                        </option>
                    ))}
                </select>

            </div>

            <br />

            <div>

                <label>Delivery Address</label>

                <br />

                <textarea
                    name="delivery_address"
                    rows="3"
                    value={formData.delivery_address}
                    onChange={onChange}
                    required
                />

            </div>

            <br />

            <div>

                <button
                    type="button"
                    onClick={onUseCurrentLocation}
                >
                    Use Current Location
                </button>

            </div>

            <br />

            <div>

                <label>Latitude</label>

                <br />

                <input
                    type="text"
                    value={formData.latitude}
                    readOnly
                />

            </div>

            <br />

            <div>

                <label>Longitude</label>

                <br />

                <input
                    type="text"
                    value={formData.longitude}
                    readOnly
                />

            </div>

            <hr />

            <div>

                <label>Notes</label>

                <br />

                <textarea
                    rows="4"
                    name="notes"
                    value={formData.notes}
                    onChange={onChange}
                />

            </div>

            <br />

            <button
                type="submit"
                disabled={loading}
            >
                {loading
                    ? "Submitting..."
                    : "Submit Request"}
            </button>

        </form>
    );
}