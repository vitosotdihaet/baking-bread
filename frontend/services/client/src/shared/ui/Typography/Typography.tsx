import Link from 'next/link';
import {
    FC,
    HTMLAttributes,
    memo,
    ReactNode,
} from 'react';
import {
    Additional,
    classNames,
    Mods,
} from 'shared/lib/classNames/classNames';
import cls from './Typography.module.scss';

type TypographyVariant = 'p' | 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'div' | 'span';
type TypographyAlign = 'center' | 'right' | 'left' | 'inherit';
type TypographyFamily = 'gt' | 'sans';
type TypographyColor = 'primary' | 'secondary' | 'accent' | 'soft' | 'disabled';
type TypographytSize = 'xs' | 'sm' | 'md' | 'lg' | 'xl';
type TypographyHeaderTag = 'h1' | 'h2' | 'h3' | 'h4' | 'h5';
type TypographyAs = 'a';

const mapSizeToHeaderTag: Record<TypographytSize, TypographyHeaderTag> = {
    xs: 'h5',
    sm: 'h4',
    md: 'h3',
    lg: 'h2',
    xl: 'h1',
};

interface TypographyProps extends HTMLAttributes<HTMLElement> {
    className?: string;
    children?: ReactNode;
    variant?: TypographyVariant;
    align?: TypographyAlign;
    family?: TypographyFamily;
    color?: TypographyColor;
    size?: TypographytSize;
    title?: string;
    noWrap?: boolean;
    fullWidth?: boolean;
    bold?: boolean;
    as?: TypographyAs;
    href?: string;
}

export const Typography: FC<TypographyProps> = memo((props: TypographyProps) => {
    const {
        className,
        children,
        variant = 'p',
        align = 'left',
        family = 'gt',
        color = 'primary',
        size = 'md',
        title,
        noWrap,
        fullWidth,
        bold,
        as,
        href,
        ...otherProps
    } = props;

    const HeaderTag = mapSizeToHeaderTag[size];
    const ContentTag = variant || 'p';

    const mods: Mods = {
        [cls.noWrap]: noWrap,
        [cls.bold]: bold,
        [cls.fullWidth]: fullWidth,
    };

    const additional: Additional = [
        cls[variant],
        cls[align],
        cls[family],
        cls[color],
        cls[size],
        className,
    ];

    if (as === 'a' && href) {
        return (
            <Link
                href={href}
                className={classNames(cls.Button, mods, additional)}
                {...otherProps}
            >
                {title && (
                    <HeaderTag
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {title}
                    </HeaderTag>
                )}
                {children && (
                    <ContentTag
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </ContentTag>
                )}
            </Link>
        );
    }

    return (
        <>
            {title && (
                <HeaderTag
                    className={classNames(cls.Typography, mods, additional)}
                    {...otherProps}
                >
                    {title}
                </HeaderTag>
            )}
            {children && (
                <ContentTag
                    className={classNames(cls.Typography, mods, additional)}
                    {...otherProps}
                >
                    {children}
                </ContentTag>
            )}
        </>
    );
});
