import Hero from "../../../components/common/Hero";
import Services from "../../../components/common/Services";
import HowItWorks from "../../../components/common/HowItWorks";
import WhyChooseUs from "../../../components/common/WhyChooseUs";
import ContactSection from "../../../components/common/ContactSection";

export default function Home() {
    return (
        <>
            <Hero />

            <Services />

            <HowItWorks />

            <WhyChooseUs />

            <ContactSection />
        </>
    );
}