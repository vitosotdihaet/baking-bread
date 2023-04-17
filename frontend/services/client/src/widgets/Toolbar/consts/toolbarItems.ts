import { BookIcon, CartIcon, HomeIcon } from 'shared/assets/icons';

export interface ToolbarItem {
    path: string;
    Icon: SvgIconType;
    label: string;
}

export const toolbarItems: ToolbarItem[] = [
    {
        path: '/home',
        Icon: HomeIcon,
        label: 'Discover',
    },
    {
        path: '/',
        Icon: BookIcon,
        label: 'Menu',
    },
    {
        path: '/cart',
        Icon: CartIcon,
        label: 'Your cart',
    },
];
