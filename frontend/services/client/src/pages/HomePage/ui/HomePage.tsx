import { FC, useState } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import { useTranslation } from 'next-i18next';
import { StateSchema } from 'app/providers/StoreProvider';
import { useSelector } from 'react-redux';
import Link from 'next/link';

interface HomePageProps {
    className?: string;
}

const HomePage: FC<HomePageProps> = (props) => {
    const { className } = props;
    const { t } = useTranslation();
    const userData = useSelector((state: StateSchema) => state.userState?.data || []);

    return (
        <div className={classNames('', {}, [className])}>
            {t('HomePage')}
            {userData && userData?.map(({ id, title }) => (
                <div key={id}>
                    {id}
                    {' '}
                    {title}
                </div>
            ))}
            <Link href='/auth'>{t('Auth')}</Link>
        </div>
    );
};

export default HomePage;
