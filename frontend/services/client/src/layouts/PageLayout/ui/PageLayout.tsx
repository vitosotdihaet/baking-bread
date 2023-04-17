import { ReactNode } from 'react';
import { Navbar } from 'widgets/Navbar';
import { Toolbar } from 'widgets/Toolbar';

export const PageLayout = ({ children }: { children: ReactNode }) => {
    return (
        <>
            <Navbar />
            {children}
            <Toolbar />
        </>
    );
};
