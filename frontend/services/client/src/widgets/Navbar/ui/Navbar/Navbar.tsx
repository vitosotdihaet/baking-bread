import { useTranslation } from 'next-i18next';
import { FC } from 'react';
import { useSelector } from 'react-redux';
import { getGoodsWithType } from 'widgets/Navbar/api/goodsTypeApi';
import { GoodTypeScroller } from 'features/goodTypeScroller';
import { LocationIcon, SearchIcon } from 'shared/assets/icons';
import { classNames } from 'shared/lib/classNames/classNames';
import { AppLink } from 'shared/ui/AppLink/AppLink';
import { Icon } from 'shared/ui/Icon/Icon';
import { Row } from 'shared/ui/Stack';
import { Typography } from 'shared/ui/Typography/Typography';

import cls from './Navbar.module.scss';

interface NavbarProps {
    className?: string;
}

export const Navbar: FC<NavbarProps> = (props) => {
    const { className } = props;
    const { t } = useTranslation();
    const { data } = useSelector(getGoodsWithType.select());

    if (!data) {
        return null;
    }

    return (
        <nav className={classNames(cls.nav, {}, [className])}>
            <Row
                justify='between'
                align='center'
                className={cls.navTop}
            >
                <Icon SVG={LocationIcon} className={cls.locationIcon} />
                <div className={cls.deliveryInfo}>
                    <AppLink className={cls.black} href='/'>
                        <Typography
                            variant='h5'
                            size='md'
                            title={t<string>('Highland Village, TX')}
                            bold
                        />
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
            <GoodTypeScroller goodTypes={data} />
        </nav>
    );
};
