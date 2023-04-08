import Link, { LinkProps } from 'next/link';
import {
    FC,
    ReactNode,
    memo,
} from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import cls from './AppLink.module.scss';

type AppLinkVariant = 'primary' | 'secondary' | 'accent' | 'soft';

interface AppLinkProps extends LinkProps {
    className?: string;
    children: ReactNode;
    variant?: AppLinkVariant;
}

export const AppLink: FC<AppLinkProps> = memo((props: AppLinkProps) => {
    const {
        className,
        children,
        href,
        variant = 'primary',
        ...otherProps
    } = props;

    return (
        <Link
            href={href}
            className={classNames(cls.AppLink, {}, [className, cls[variant]])}
            {...otherProps}
        >
            {children}
        </Link>
    );
});
