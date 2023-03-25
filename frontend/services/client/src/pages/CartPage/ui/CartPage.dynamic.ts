import dynamic from 'next/dynamic';

export const CartPageDynamic = dynamic(() => import('./CartPage'));
