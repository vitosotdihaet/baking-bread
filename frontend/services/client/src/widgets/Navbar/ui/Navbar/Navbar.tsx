import { useTranslation } from 'next-i18next';
import { FC } from 'react';
import { LocationIcon, SearchIcon } from 'shared/assets/icons';
import { classNames } from 'shared/lib/classNames/classNames';
import { AppLink } from 'shared/ui/AppLink/AppLink';
import { Icon } from 'shared/ui/Icon/Icon';
import { Row } from 'shared/ui/Stack';
import { Typography } from 'shared/ui/Typography/Typography';
import { NavbarScroller } from '../NavbarScroller/NavbarScroller';

import cls from './Navbar.module.scss';

interface NavbarProps {
    className?: string;
}

export const Navbar: FC<NavbarProps> = (props) => {
    const { className } = props;
    const { t } = useTranslation();

    return (
        <div className={classNames(cls.nav, {}, [className])}>
            <Row
                justify='between'
                align='center'
                className={cls.navTop}
            >
                <Icon SVG={LocationIcon} className={cls.locationIcon} />
                <div className={cls.deliveryInfo}>
                    <AppLink href='/'>
                        <Typography variant='h3' bold>{t('Highland Village, TX')}</Typography>
                    </AppLink>
                    <Typography
                        className={cls.deliveryTime}
                        variant='div'
                        color='disabled'
                        size='sm'
                    >
                        {t('~25 minute delivery')}
                    </Typography>
                </div>
                <Icon SVG={SearchIcon} />
            </Row>
            <NavbarScroller />
        </div>
    );
};
