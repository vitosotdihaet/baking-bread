import dynamic from 'next/dynamic';

export const HomePageDynamic = dynamic(() => import('./HomePage'));
