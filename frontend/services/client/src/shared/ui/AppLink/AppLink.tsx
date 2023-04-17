import Link, { LinkProps } from 'next/link';
import {
    FC,
    ReactNode,
    memo,
} from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import cls from './AppLink.module.scss';

type AppLinkVariant = 'primary' | 'secondary' | 'accent' | 'soft' | 'disabled';
type AppLinkSize = 'xs' | 'sm' | 'md' | 'lg' | 'xl';

interface AppLinkProps extends LinkProps {
    className?: string;
    children: ReactNode;
    variant?: AppLinkVariant;
    size?: AppLinkSize;
    nounderlined?: boolean;
}

export const AppLink: FC<AppLinkProps> = memo((props: AppLinkProps) => {
    const {
        className,
        children,
        href,
        variant = 'primary',
        size = 'md',
        nounderlined,
        ...otherProps
    } = props;

    return (
        <Link
            href={href}
            className={classNames(cls.AppLink, { [cls.nounderlined]: nounderlined }, [cls[variant], cls[size], className])}
            {...otherProps}
        >
            {children}
        </Link>
    );
});
